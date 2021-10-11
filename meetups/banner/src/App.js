import logo from './simplycruit.png';
import './App.css';
import background from './background.jpg'
import gitlab from './gitlab.png'

function App() {
  return (
    <div className="background" style={{ backgroundImage: `url(${background})` }}>
      <div className="backdrop">
        <h2>How to Build:</h2>
        <div className="border">
          <h1>Fyne</h1>
          <p>Graphic User Interface Library</p>
        </div>
      </div>
    </div>
  );
}

export default App;
