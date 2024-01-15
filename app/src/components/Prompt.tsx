import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { Form, FormField, FormControl, FormMessage, FormItem, FormLabel } from './ui/form';
import { Textarea } from './ui/textarea';
import { Button } from './ui/button';
import { PromptSchema, promptSchema } from '@/lib/validators';
import { Loader2 } from 'lucide-react'
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from './ui/select';

type PromptProps = {
  onSubmit: (data: PromptSchema) => void;
  isLoading?: boolean;
};

function Prompt({ onSubmit, isLoading }: PromptProps) {

  const form = useForm<PromptSchema>({
    resolver: zodResolver(promptSchema),
    defaultValues: {
      model: "1",
      text: '',
    },
  });

  return (
    <section>
      <Form {...form}>
        <form onSubmit={form.handleSubmit(onSubmit)} className="flex flex-col items-end gap-2">
        <FormField
            control={form.control}
            name="model"
            render={({ field }) => (
              <FormItem className="w-full">
                <FormLabel htmlFor={field.name}>Select model</FormLabel>
                <Select onValueChange={field.onChange} defaultValue={field.value}>
                  <FormControl>
                    <SelectTrigger>
                      <SelectValue placeholder="Select model" />
                    </SelectTrigger>
                  </FormControl>
                  <SelectContent>
                    <SelectItem value="1">Model 1 (57 features)</SelectItem>
                    <SelectItem value="2">Model 2 (3000 features)</SelectItem>
                  </SelectContent>
                </Select>
                <FormMessage />
              </FormItem>
            )}
          />
          <FormField
            control={form.control}
            name="text"
            render={({ field }) => (
              <FormItem className="w-full">
                <FormLabel htmlFor={field.name}>Insert email body</FormLabel>
                <FormControl>
                  <Textarea rows={6} placeholder="Dear..." {...field} />
                </FormControl>
                <FormMessage />
              </FormItem>
            )}
          />
          <Button disabled={isLoading} type="submit" className="">
            {isLoading && <Loader2 className="mr-2 h-4 w-4 animate-spin" />}
            Predict
          </Button>
        </form>
      </Form>
    </section>
  );
}

export default Prompt;