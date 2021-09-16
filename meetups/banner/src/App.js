import logo from './simplycruit.png';
import './App.css';
import background from './background.jpg'
import gitlab from './gitlab.png'

function App() {
  return (
    <div className="background" style={{ backgroundImage: `url(${background})` }}>
      <div className="backdrop">
        <h2>How Is It Built:</h2>
        <div className="border">
          <img className="logo" src={logo} />
        </div>
      </div>
      <img className="gitlab" src={gitlab} />
    </div>
  );
}

export default App;
