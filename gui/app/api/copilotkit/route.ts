import { NextRequest } from "next/server";
import {
  CopilotRuntime,
  copilotRuntimeNextJSAppRouterEndpoint,
  GoogleGenerativeAIAdapter,
} from "@copilotkit/runtime";

const serviceAdapter = new GoogleGenerativeAIAdapter({
  model: "gemini-1.5-flash",
});

const runtime = new CopilotRuntime({
  remoteEndpoints: [
    {
      url: "http://localhost:8000/copilotkit",
    },
  ],
});

export const POST = async (req: NextRequest) => {
  const { handleRequest } = copilotRuntimeNextJSAppRouterEndpoint({
    runtime,
    serviceAdapter,
    endpoint: "/api/copilotkit",
  });

  return handleRequest(req);
};
