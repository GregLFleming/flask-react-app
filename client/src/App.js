import logo from './logo.svg';
import './App.css';
import NavBar from './Components/navBar';
import HomePage from './Components/homePage';
import { RecoilRoot } from 'recoil';


function App() {
  return (
    <RecoilRoot>
    <div className="App">
      <NavBar />
      <HomePage />
    </div> 
    </RecoilRoot>
  );
}


export default App;
