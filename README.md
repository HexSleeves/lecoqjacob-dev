# Jacob LeCoq's Personal Website & Blog

## Features

- ✨ Retro-inspired, fully responsive design
- 🌗 Dark & light mode
- 🎨 Easily customizable colors and text
- 🧑‍💻 TypeScript & TailwindCSS
- 🏆 100/100 Lighthouse score
- ♿ Accessible and SEO-friendly
- 📝 Blog and project sections

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/astro-personal.git
cd astro-personal
```

### 2. Install Dependencies

> **Note:** This project uses `bun` for package management.

```bash
bun install
```

### 3. Run the Development Server

```bash
bun dev
```

Visit [localhost:4321](http://localhost:4321) to view your site locally.

---

## Customization

### Site Metadata & Text

All site metadata (name, social links, descriptions, menu, etc.) is managed in [`src/lib/variables.ts`](src/lib/variables.ts).
Update this file to personalize your username, profile image, social links, blog/project titles, and more.

```typescript
export const GLOBAL = {
  username: "HexSleeves",
  rootUrl: "https://hex-sleeves.dev",
  shortDescription: "Fullstack Developer",
  // ...more fields
};
```

---

## Deployment

This site is deployed on [Vercel](https://vercel.com/).
You can deploy your own fork by connecting your repo to Vercel and following their setup instructions.

---

## License

MIT

---

## Credits

- [Astro](https://astro.build/)
- [Charca Blog Template](https://github.com/Charca/astro-blog-template) (used as a base and customized for this site)

---

## 👀 Want to learn more?

Feel free to check [Astro's documentation](https://github.com/withastro/astro) or jump into Astro's [Discord server](https://astro.build/chat).
