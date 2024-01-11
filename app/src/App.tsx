import Prediction from './components/Prediction';
import Prompt from './components/Prompt';
import { useMutation } from 'react-query';
import { ClassifierApi } from './api/predict';

function App() {

  const predict = useMutation({
    mutationFn: ClassifierApi.predict
  });

  return (
    <main className="min-h-screen py-8 px-4 sm:px-0">
      <div className="w-full max-w-lg mx-auto space-y-8">
        <header className="flex items-center space-x-8 fixed top-0 bg-white py-4 w-full">
          <h1 className="text-lg font-bold">email-classifier</h1>
        </header>
        <Prompt onSubmit={predict.mutateAsync} />
        {predict.isSuccess && <Prediction prediction={predict.data.prediction} />}
      </div>
    </main>
  );
}

export default App;
