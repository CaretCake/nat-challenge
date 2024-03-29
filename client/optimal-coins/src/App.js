import { Header } from './components/Header.js'
import { OptimalCoins } from './components/OptimalCoins.js'
import './App.css';

function App() {
  return (
    <div className="App">
      <Header/>
      <div className="Container">
        <OptimalCoins/>
      </div>
    </div>
  );
}

export default App;
