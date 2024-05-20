import { BrowserRouter, Routes, Route} from "react-router-dom";
import Layout from "./Layout";
import Home from "./Home";
import Upload from "./Upload";
import Search from "./Search";
import Footer from "./Footer";
import './App.css';

function App() {
  return  ( <>
    <BrowserRouter>
    <Layout/>
    <Routes>
        <Route path="/" element={<Home/>}/>
        <Route path='/Upload' element={<Upload/>}/>
        <Route path='/Search' element={<Search/>}/>
    </Routes>
  </BrowserRouter>
  <Footer/>
  </>
);
}

export default App;
