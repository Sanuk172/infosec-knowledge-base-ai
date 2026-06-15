import { defineConfig } from "vitepress";

export default defineConfig({
  base: "/infosec-knowledge-base-ai/",
  lang: "ru-RU",
  title: "Knowledge Base",
  description: "Каркас базы знаний с AI-ассистентом",
  cleanUrls: true,
  themeConfig: {
    logo: "/logo.svg",
    nav: [
      { text: "Главная", link: "/" },
      { text: "Базы данных", link: "/threats/" },
      { text: "AI Ассистент", link: "/assistant/" }
    ],
    sidebar: [
      {
        text: "Базы данных",
        collapsed: false,
        items: [
          { text: "Угрозы БДУ ФСТЭК", link: "/threats/" }
        ]
      },
      {
        text: "Ассистент",
        items: [{ text: "AI Ассистент", link: "/assistant/" }]
      }
    ],
    footer: {
      message: "Контент добавляется командой проекта",
      copyright: "Copyright © 2026"
    }
  }
});
