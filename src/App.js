import { HashRouter as Router, Routes, Route } from 'react-router-dom';
import Photos from "./components/photos";

function App() {
    return (
      <Router>
        <Routes>
          <Route path="/" element={<Photos/>}/>
        </Routes>
      </Router>  
    );
}

export default App;
