import { Header } from './Header.js'
import { OptimalCoins } from './OptimalCoins.js'
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
