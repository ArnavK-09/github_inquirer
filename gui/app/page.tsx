"use client";

import { CopilotKit } from "@copilotkit/react-core";
import { CopilotChat, CopilotKitCSSProperties } from "@copilotkit/react-ui";
import "@copilotkit/react-ui/styles.css";
import App from "./app/page";

export default function Home() {
  return (
    <>
      <CopilotKit runtimeUrl="/api/copilotkit" agent="github_inquirer">
        <App />
      </CopilotKit>
    </>
  );
}
