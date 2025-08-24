---
title: Personal Portfolio Website
slug: astro-personal-website
description: Modern personal website built with Astro, featuring blog functionality and project showcases
excerpt: A fast, modern personal website showcasing projects and blog posts with excellent SEO and performance
tags: ["portfolio", "website", "personal"]
techStack: ["Astro", "TypeScript", "Svelte", "MDX", "CSS"]
githubUrl: https://github.com/HexSleeves/lecoqjacob-dev
liveUrl: https://hexsleeves.github.io/personal-website/
featured: true
publishDate: 2025-08-05
images: [
  "/assets/projects/personal-website-hero.jpg",
  "/assets/projects/personal-website-blog.jpg",
  "/assets/projects/personal-website-projects.jpg"
]
---

## Project Overview

This personal portfolio website was built using Astro's static site generation capabilities, combining modern web technologies to create a fast, accessible, and SEO-optimized online presence.

## Key Features

- **Static Site Generation**: Built with Astro for optimal performance and SEO
- **Blog Integration**: Full-featured blog with MDX support and reading time estimates
- **Project Showcase**: Dynamic project listings with filtering and categorization
- **Theme System**: Dark/light mode toggle with system preference detection
- **Performance Optimized**: Lighthouse scores of 100 across all metrics

## Technical Implementation

The site leverages Astro's content collections for type-safe content management, with Svelte components for interactive elements like the theme toggle. The styling uses modern CSS custom properties for theming, and the build process generates optimized static files for deployment.

## Architecture Decisions

- **Content Collections**: Used Astro's content collections with Zod schemas for type-safe frontmatter validation
- **Partial Hydration**: Only interactive components (theme toggle) are hydrated client-side
- **Font Optimization**: Self-hosted fonts with proper preloading for better performance
- **SEO Strategy**: Comprehensive meta tags, structured data, and social media optimization
