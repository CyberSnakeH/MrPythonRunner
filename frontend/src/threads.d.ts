// threads 1.7 publishes declarations but omits their entry in package exports.
declare module 'threads' {
  export const spawn: typeof import('../node_modules/threads/dist/master').spawn;
  export const Thread: typeof import('../node_modules/threads/dist/master').Thread;
  export type ModuleThread<T extends Record<string, (...args: never[]) => unknown>> = import('../node_modules/threads/dist/master').ModuleThread<T>;
}
