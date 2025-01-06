import { Star, GitFork, Circle } from "lucide-react";
import {
  Card,
  CardContent,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import Link from "next/link";

interface GitHubRepoCardProps {
  name: string | null;
  description: string | null;
  license?: string | null;
  author?: string | null;
}

export default function GitHubRepoCard({
  name,
  description,
  license,
  author,
}: GitHubRepoCardProps) {
  return (
    <Link href={`https://github.com/${name}`} target="_blank">
      <Card className="h-full w-full max-w-md border-4 border-primary mx-auto bg-zinc-950 shadow-lg hover:shadow-xl transition-shadow duration-300">
        <CardHeader>
          <CardTitle className="text-lg font-extrabold text-primary">
            {name ?? "repo/name"}
          </CardTitle>
        </CardHeader>
        <CardContent>
          <p className="text-sm text-primary/80 mb-4">
            {description ?? "No description..."}
          </p>
          <div className="flex items-center space-x-4 text-sm text-gray-500 dark:text-gray-400">
            <div className="flex items-center">
              <Circle className="w-3 h-3 mr-1 fill-primary" />
              <span>{author}</span>
            </div>
            <div className="flex items-center">
              <GitFork className="w-4 h-4 mr-1" />
              <span>{license ?? "No License"}</span>
            </div>
          </div>
        </CardContent>
        <CardFooter>
          <Button
            variant="outline"
            className="w-full text-primary border-primary hover:shadow-lg transition-all ease-in-out"
          >
            View Repository
          </Button>
        </CardFooter>
      </Card>
    </Link>
  );
}
