import logo from './logo.svg';
import { Header } from './Header.js'
import { DollarForm } from './DollarForm.js'
import { CoinCount } from './CoinCount.js'
import './App.css';

function App() {
  return (
    <div className="App">
      <Header/>
      <div className="Container">
        <DollarForm/>
        <CoinCount/>
      </div>
    </div>
  );
}

export default App;
