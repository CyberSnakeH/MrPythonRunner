import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import { Children, isValidElement } from 'react';
import { TikzDiagram } from './TikzDiagram';

export function Statement({ text, assets }: { text: string; assets: Record<string, string> }) {
  return <div className="prose-statement"><ReactMarkdown remarkPlugins={[remarkGfm, remarkMath]} rehypePlugins={[[rehypeKatex, { trust: false, strict: 'warn' }]]}
    urlTransform={url => url.startsWith('assets/') || url.startsWith('#') ? url : ''}
    components={{
      pre: ({ children }) => {
        const child = Children.toArray(children)[0];
        if (isValidElement<{ className?: string; children?: string }>(child)
          && /^language-(tikz|tikzjax)$/.test(child.props.className || '')
          && typeof child.props.children === 'string') {
          return <TikzDiagram source={child.props.children.trimEnd()} />;
        }
        return <pre>{children}</pre>;
      },
      img: ({ src, alt }) => {
        const name = src || '';
        if (!assets[name]) return <span className="muted">[Image absente : {alt || name}]</span>;
        const ext = name.split('.').pop();
        const mime = ext === 'jpg' ? 'jpeg' : ext;
        return <img src={`data:image/${mime};base64,${assets[name]}`} alt={alt || ''} />;
      },
      a: ({ children }) => <span className="statement-link">{children}</span>,
    }}>{text || '*L’énoncé apparaîtra ici.*'}</ReactMarkdown></div>;
}
