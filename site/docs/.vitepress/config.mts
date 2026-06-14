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
      { text: "Угрозы БДУ", link: "/threats/" },
      { text: "Разделы", link: "/guide/" },
      { text: "AI Ассистент", link: "/assistant/" }
    ],
    sidebar: [
      {
        text: "База угроз ФСТЭК",
        collapsed: false,
        items: [
          { text: "Все угрозы", link: "/threats/" }
        ]
      },
      {
        text: "Разделы",
        items: [
          { text: "Обзор", link: "/guide/" },
          { text: "Теория и стандарты", link: "/guide/section-1" },
          { text: "Практика и инструкции", link: "/guide/section-2" }
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
