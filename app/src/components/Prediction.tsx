type PredictionProps = {
  prediction: 0 | 1;
};

function Prediction({ prediction }: PredictionProps) {
    
  return (
    <section>
      <p>Prediction: {
        prediction === 0 ? 
          <span className="text-green-600 font-bold text-lg">Not spam</span> : 
          <span className="text-red-600 font-bold text-lg">Spam</span>
      }</p>
    </section>
  );
}

export default Prediction;