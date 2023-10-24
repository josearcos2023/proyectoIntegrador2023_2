import './App.css';
import {BrowserRouter, Routes, Route} from 'react-router-dom';
import {Register} from "./component/register"
import {Login} from "./component/login";
import {Home} from "./component/Home";
import {Navigation} from './component/navigation';
import {Logout} from './component/logout';
function App() {
    return <BrowserRouter>
    <Navigation></Navigation>
        <Routes>
            <Route path="/" element={<Home/>}/>
            <Route path="/login" element={<Login/>}/>
            <Route path="/logout" element={<Logout/>}/>
            <Route path="/register" element={<Register/>}/>
        </Routes>
    </BrowserRouter>;
}

export default App;
