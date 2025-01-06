"use client";
import { CopilotPopup } from "@copilotkit/react-ui";
import { FormEvent, useEffect, useState } from "react";
import { useCoAgent } from "@copilotkit/react-core";
import GitHubRepoCard from "@/components/card";
import { useCopilotChat } from "@copilotkit/react-core";
import { Role, TextMessage } from "@copilotkit/runtime-client-gql";
import { Button } from "@/components/ui/button";
import { CopilotKit } from "@copilotkit/react-core";
interface YourAgentState {
  messages: string[]; // Messages associated with the workflow
  query?: string; // Query generated or received from the user
  repos?: any[]; // List of repository data
  summary?: string; // Summary of the results
  output?: string; // Final output of the workflow
}

export interface GithubRepository {
  name: string;
  full_name: string | null;
  owner: {
    login: string | null;
    id: number | null;
    html_url: string | null;
  } | null;
  description: string | null;
  url: string | null;
  license: {
    key: string | null;
    name: string | null;
    url: string | null;
  } | null;
}

export default function App() {
  const [isLoading, setLoading] = useState(false);
  const [query, setQuery] = useState("");
  const [repos, setRepos] = useState<GithubRepository[]>([]);
  const {
    visibleMessages,
    appendMessage,
    setMessages,
    deleteMessage,
    reloadMessages,
    stopGeneration,
    isLoading: isCopilotLoading,
  } = useCopilotChat();

  const { state } = useCoAgent<YourAgentState>({
    name: "github_inquirer",
  });
  useEffect(() => {
    if (state.repos?.length) {
      setRepos(state?.repos as GithubRepository[]);
    }
    console.log(state, visibleMessages);
  }, [state]);
  async function handleQuery(e: FormEvent<HTMLFormElement>) {
    e?.preventDefault();
    setLoading(true);

    await appendMessage(new TextMessage({ content: query, role: Role.User }));
    setLoading(false);
  }

  return (
    <>
      <CopilotPopup />
      <section
        className={`${repos.length == 0 ? "h-screen" : ""} w-screen py-10`}
      >
        <div
          className={`${repos.length == 0 ? "h-full" : ""} w-full grid place-items-center`}
        >
          <div className="grid w-full max-w-xl items-center gap-1.5">
            <form onSubmit={handleQuery}>
              <input
                type="input"
                max={500}
                value={query} // Bind the input value to the state variable
                onChange={(e) => setQuery(e.target.value)} // Update the state on change
                placeholder="Enter Query..."
                disabled={isLoading || isCopilotLoading}
                className={`rounded-lg w-full disabled:bg-white/10 text-4xl px-5 py-3 text-primary focus:border-2 focus:outline-primary tracking-normal bg-transparent border-2 border-primary font-inherit`}
              />
            </form>
            <div className="text-primary/80 text-lg tracking-tighter transition-all ease-in-out justify-center text-center py-5 font-bold">
              {state.output ?? ""}
            </div>
          </div>
        </div>
      </section>

      <section className="pt-5">
        {(isLoading || isCopilotLoading) && repos.length == 0 && (
          <div className="overflow-hidden">
            <div className="text-primary grid place-items-center font-extrabold text-5xl animate-spin">
              *
            </div>
          </div>
        )}

        <div className="gap-4 grid grid-cols-1 md:grid-cols-2 w-full px-auto">
          {repos.map((repo, i) => (
            <GitHubRepoCard
              key={i}
              name={repo.full_name}
              description={repo.description}
              license={repo.license?.name}
              author={repo.owner?.login}
            />
          ))}
        </div>
      </section>
    </>
  );
}
