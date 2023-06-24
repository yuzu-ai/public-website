import shortcodes from "@/shortcodes/all";
import { MDXRemote } from "next-mdx-remote/rsc";
import remarkGfm from "remark-gfm";
import rehypeKatex from 'rehype-katex';
import remarkMath from 'remark-math'
import rehypeHighlight from 'rehype-highlight'

const MDXContent = ({ content }: { content: any }) => {
  const mdxOptions = {
    remarkPlugins: [remarkGfm, remarkMath],
    rehypePlugins: [rehypeKatex, rehypeHighlight],
  };
  return (
    <>
      {/* @ts-expect-error Async Server Component */}
      <MDXRemote
        source={content}
        components={shortcodes}
        options={{ mdxOptions }}
      />
    </>
  );
};

export default MDXContent;
