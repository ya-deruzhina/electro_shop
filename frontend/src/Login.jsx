import React, { useState } from "react";

function Login({ onLogin }) {
  const [identity, setIdentity] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    const response = await fetch("http://127.0.0.1:8000/api/v1/users/sign_in/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ identity, password }),
    });

    const data = await response.json();

    if (response.ok) {
      localStorage.setItem("token", data.token);  
      onLogin();
    } else {
      alert("Ошибка авторизации");
    }
  };

  return (
    <form onSubmit={handleSubmit} style={{ padding: "40px" }}>
      <h2>Авторизация</h2>
      <input
        type="text"
        placeholder="Логин"
        value={identity}
        onChange={(e) => setIdentity(e.target.value)}
      /><br /><br />
      <input
        type="password"
        placeholder="Пароль"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      /><br /><br />
      <button type="submit">Войти</button>
    </form>
  );
}

export default Login;