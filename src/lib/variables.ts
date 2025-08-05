// Set any item to undefined to remove it from the site or to use the default value

export const GLOBAL = {
  // Site metadata
  username: "Jacob",
  rootUrl: "https://lecoqjacob.dev",
  shortDescription: "Fullstack Developer",
  longDescription:
    "Jacob LeCoq is a fullstack developer passionate about creating beautiful, performant web applications using modern technologies.",

  // Social media links
  githubProfile: "https://github.com/HexSleeves",
  twitterProfile: "https://x.com/jacob_lecoq",
  linkedinProfile: "https://www.linkedin.com/in/jacob-lecoq",

  // Common text names used throughout the site
  articlesName: "Blog",
  projectsName: "Projects",
  viewAll: "View All",

  // Common descriptions used throughout the site
  noArticles: "No blog posts yet.",
  noProjects: "No projects yet.",

  // Blog metadata
  blogTitle: "Blog",
  blogShortDescription: "Thoughts on web development and technology.",
  blogLongDescription:
    "Articles about web development, programming insights, and the latest in tech.",

  // Project metadata
  projectTitle: "Projects",
  projectShortDescription:
    "A collection of my web development projects and experiments.",
  projectLongDescription:
    "Showcase of my work including frontend applications, full-stack projects, and open source contributions.",

  // Profile image
  profileImage: "profile-pic.webp",

  // Menu items
  menu: {
    home: "/",
    about: "/about",
    projects: "/projects",
    blog: "/blog",
  },
};

// SEO and structured data
export const SEO = {
  jsonLd: {
    "@context": "https://schema.org",
    "@type": "Person",
    name: GLOBAL.username,
    jobTitle: GLOBAL.shortDescription,
    description: GLOBAL.longDescription,
    url: GLOBAL.rootUrl,
    image: `${GLOBAL.rootUrl}/assets/${GLOBAL.profileImage}`,
    sameAs: [
      GLOBAL.githubProfile,
      GLOBAL.twitterProfile,
      GLOBAL.linkedinProfile,
    ].filter(Boolean),
    knowsAbout: [
      "Web Development",
      "Full Stack Development",
      "TypeScript",
      "JavaScript",
      "Astro",
      "React",
      "Svelte",
      "Node.js",
    ],
  },
};
