import axios from "axios";
import React, { useState } from "react";
import { useNavigate } from 'react-router-dom';


export const Register = () => {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();



  const submit = async (e) => {
    e.preventDefault();

    const user = {
      username: username,
      email: email,
      password: password
    };

    try {
      const { data } = await axios.post('http://localhost:8000/register/', user, {
        headers: {
          'Content-Type': 'application/json'
        }
      });

      navigate('/login');

      console.log(data);

    } catch (error) {
      console.error(error);

    }
  };


  return (
    <div className="Auth-form-container">
      <form className="Auth-form" onSubmit={submit}>
        <div className="Auth-form-content">
          <h3 className="Auth-form-title">Registro</h3>
          <div className="form-group mt-3">
            <label>Username</label>
            <input
              className="form-control mt-1"
              placeholder="Ingrese su nombre de usuario"
              name='username'
              type='text'
              value={username}
              required
              onChange={e => setUsername(e.target.value)}
            />
          </div>
          <div className="form-group mt-3">
            <label>Email</label>
            <input
              className="form-control mt-1"
              placeholder="Ingrese su correo"
              name='email'
              type='email'
              value={email}
              required
              onChange={e => setEmail(e.target.value)}
            />
          </div>
          <div className="form-group mt-3">
            <label>Contraseña</label>
            <input
              name='password'
              type="password"
              className="form-control mt-1"
              placeholder="Ingrese su contraseña"
              value={password}
              required
              onChange={e => setPassword(e.target.value)}
            />
          </div>
          <div className="d-grid gap-2 mt-3">
            <button type="submit" className="btn btn-primary">
              Registrar
            </button>
          </div>
        </div>
      </form>
    </div>
  );
};