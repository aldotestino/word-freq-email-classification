import * as z from 'zod';

export const promptSchema = z.object({
  model: z.string(),
  text: z.string().min(10)
});

export type PromptSchema = z.infer<typeof promptSchema>;