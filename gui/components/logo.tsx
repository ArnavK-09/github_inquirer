"use client";

import { Button } from "@/components/ui/button";

export default function Logo() {
  return (
    <div className="absolute top-0 py-2">
      <div className="w-screen grid place-items-center">
        <Button
          onClick={() => {
            window.location.href = "https://github.com/ArnavK-09";
          }}
          className="font-extrabold px-4 tracking-tight shadow-lg"
        >
          Github Inquirer
        </Button>
      </div>
    </div>
  );
}
