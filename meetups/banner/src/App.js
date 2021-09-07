import logo from './simplycruit.png';
import './App.css';
import background from './background.jpg'

function App() {
  return (
    <div className="background" style={{ background: `url(${background})` }}>
      <div className="backdrop">
        <h2>How Is It Built:</h2>
        <div className="border">
          <img className="logo" src={logo} />
        </div>
      </div>
    </div>
  );
}

export default App;
