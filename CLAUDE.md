# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Common Development Commands

```bash
# Development server (uses bun, not npm)
bun dev           # Start development server on localhost:4321
bun start         # Alias for bun dev

# Build and deployment
bun build         # Build for production
bun preview       # Preview production build locally

# Package management
bun install       # Install dependencies (uses bun.lock)
```

## Architecture Overview

This is an **Astro-based personal website** with blog functionality, using a modern stack:

### Tech Stack
- **Astro** - Static site generator with partial hydration
- **Svelte** - Interactive components (theme toggle)
- **TypeScript** - Type safety throughout
- **MDX** - Enhanced markdown for blog posts
- **Bun** - Package manager and runtime

### Key Architecture Patterns

**Content Management**: Uses Astro's content collections with a file-based loader pointing to `src/data/blog-posts/`. Blog posts are markdown files with frontmatter schema validation via Zod.

**Configuration Centralization**: All site metadata, social links, and customizable text is centralized in `src/lib/variables.ts` with `GLOBAL` and `SEO` exports. This includes username, descriptions, menu items, and structured data.

**Layout System**: Uses a single `BaseLayout.astro` that wraps pages with consistent header/footer. The layout handles responsive design and includes SEO metadata via `BaseHead.astro`.

**Theme System**: Dark/light mode is implemented with:
- CSS custom properties for theming
- `ThemeToggleButton.svelte` for user control
- localStorage persistence with system preference fallback
- Inline script in BaseHead to prevent FOUC

**Styling**: Uses vanilla CSS with custom properties, no external CSS framework. Fonts are self-hosted and loaded via `src/styles/fonts.css`.

### Content Structure

```
src/data/blog-posts/     # Markdown blog posts
src/pages/blog/[slug].astro  # Dynamic blog post pages
src/content.config.js    # Content collection schema
```

Blog posts use static path generation with reading time calculation and are rendered with full MDX support including GFM and smart quotes.

### Customization Points

- `src/lib/variables.ts` - All site metadata and text
- `src/styles/global.css` - CSS custom properties for colors/typography
- `astro.config.mjs` - Site URL and markdown processing plugins
- `public/assets/` - Images and static assets

The site is optimized for performance with proper SEO, structured data, and social media meta tags.