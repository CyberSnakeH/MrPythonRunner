import { useEffect, useRef, useState } from 'react';
import { api, flushSaves } from './api';
import type { Report } from './types';

export function useExecution(onReport: (report: Report, code: string) => void, onError: (error: unknown) => void) {
  const [running, setRunning] = useState(false);
  const job = useRef<string | null>(null);
  const mounted = useRef(true);
  const generation = useRef(0);
  useEffect(() => { mounted.current = true; return () => { mounted.current = false; generation.current++; if (job.current) void api('jobs/cancel', { id: job.current }).catch(() => {}); }; }, []);
  const start = async (pack_id: string, exercise_id: string, code: string, student?: string) => {
    if (running) return;
    setRunning(true);
    const run = ++generation.current;
    try {
      await flushSaves();
      const response = await api<{ id: string }>('jobs/start', { pack_id, exercise_id, code, student });
      job.current = response.id;
      if (!mounted.current || run !== generation.current) { await api('jobs/cancel', { id: response.id }); return; }
      while (mounted.current && run === generation.current) {
        const state = await api<{ state: string; report: Report }>('jobs/get', { id: response.id });
        if (state.state === 'done') { onReport(state.report, code); break; }
        await new Promise(resolve => setTimeout(resolve, 180));
      }
    } catch (error) { if (mounted.current) onError(error); }
    finally { job.current = null; if (mounted.current) setRunning(false); }
  };
  const stop = () => { if (job.current) void api('jobs/cancel', { id: job.current }).catch(onError); };
  return { running, start, stop };
}
