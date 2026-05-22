import { defineConfig } from "vitepress";

export default defineConfig({
  base: "/web-site_with_ai/",
  lang: "ru-RU",
  title: "Knowledge Base",
  description: "Каркас базы знаний с AI-ассистентом",
  cleanUrls: true,
  themeConfig: {
    logo: "/logo.svg",
    nav: [
      { text: "Главная", link: "/" },
      { text: "Разделы", link: "/guide/" },
      { text: "AI Ассистент", link: "/assistant/" }
    ],
    sidebar: [
      {
        text: "Старт",
        items: [
          { text: "Обзор", link: "/guide/" },
          { text: "Раздел 1", link: "/guide/section-1" },
          { text: "Раздел 2", link: "/guide/section-2" }
        ]
      },
      {
        text: "Справка",
        items: [
          { text: "FAQ", link: "/reference/faq" },
          { text: "Шаблон статьи", link: "/reference/template" }
        ]
      },
      {
        text: "Ассистент",
        items: [{ text: "О модуле", link: "/assistant/" }]
      }
    ],
    search: {
      provider: "local"
    },
    footer: {
      message: "Контент добавляется командой проекта",
      copyright: "Copyright © 2026"
    }
  }
});
