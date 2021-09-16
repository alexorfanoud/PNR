import './App.css';
import LineChart from './components/LineChart'

function App() {
  return (
    <div className="App">
      Hello world app
      <div>
      <LineChart pk={3}/>
      {/* <LineChart pk={4}/> */}
      </div>
      

    </div>
  );
}

export default App;
