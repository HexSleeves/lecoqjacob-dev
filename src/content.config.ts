import { defineCollection, z } from "astro:content";
import { glob } from "astro/loaders";

const posts = defineCollection({
  loader: glob({ pattern: "*.md", base: "./src/data/blog-posts" }),
  schema: z.object({
    title: z.string(),
    slug: z.string(),
    publishDate: z.union([z.string(), z.date()]),
    description: z.string(),
    tags: z.array(z.string()).optional(),
    categories: z.array(z.string()).optional(),
    draft: z.boolean().optional(),
  }),
});

const projects = defineCollection({
  loader: glob({ pattern: "*.md", base: "./src/data/projects" }),
  schema: z.object({
    title: z.string(),
    slug: z.string(),
    description: z.string(),
    excerpt: z.string().optional(),
    tags: z.array(z.string()).optional(),
    techStack: z.array(z.string()).optional(),
    githubUrl: z.string().optional(),
    liveUrl: z.string().optional(),
    featured: z.boolean().optional(),
    publishDate: z.union([z.string(), z.date()]),
    images: z.array(z.string()).optional(),
    draft: z.boolean().optional(),
  }),
});

export const collections = { posts, projects };
