import type { Metadata } from "next";
import { Space_Mono as Font } from "next/font/google";
import "./globals.css";
import Logo from "@/components/logo";

export const font = Font({
  weight: "400",
  style: "normal",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "Github Inquiry",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className="dark !overflow-x-hidden">
      <body
        className={`${font.className} mx-4 antialiased min-h-screen py-10 overflow-x-hidden bg-zinc-900`}
      >
        {" "}
        <Logo />
        {children}
      </body>
    </html>
  );
}
