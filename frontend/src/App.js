import React, { useEffect, useState } from "react";
import Login from "./Login";

function App() {
  const [shops, setShops] = useState([]);
  const [isAuthenticated, setIsAuthenticated] = useState(
    !!localStorage.getItem("token")
  );

  useEffect(() => {
    if (!isAuthenticated) return;

    fetch("http://127.0.0.1:8000/api/v1/shops/", {
      headers: {
        Authorization: `${localStorage.getItem("token")}`,
      },
    })
      .then((res) => {
        if (res.status === 401) throw new Error("Unauthorized");
        return res.json();
      })
      .then((data) => setShops(data.results || []))
      .catch((err) => {
        console.error("Ошибка:", err);
        setIsAuthenticated(false); // если токен плохой — выход
      });
  }, [isAuthenticated]);

  const copyEmail = (email) => {
    navigator.clipboard.writeText(email)
      .then(() => alert("Email скопирован!"))
      .catch(() => alert("Ошибка копирования"));
  };

  if (!isAuthenticated) {
    return <Login onLogin={() => setIsAuthenticated(true)} />;
  }

  return (
    <div style={{ padding: "20px" }}>
      <h1>Список объектов сети</h1>
      {shops.map((shop) => (
        <div key={shop.id} style={{ marginBottom: "20px" }}>
          <p><strong>{shop.name}</strong> — {shop.email}</p>
          <p>Country: {shop.country}</p>
          <p>City: {shop.city}</p>
          <p>Street: {shop.street}</p>
          <p>House number: {shop.house_number}</p>
          <p>****************************</p>
          <h4>Products:</h4>
          {shop.products.map((products) => (
            <div key={products.id}>
              <p>Name: {products.name}</p>
              <p>Model: {products.model}</p>
              <p>Launch date: {products.launch_date}</p>
              <p>Created at: {products.created_at}</p>
              <p>_________________</p>
            </div>
          ))}
          <p>****************************</p>
          {shop.category_supplier && (
            <div>
              <p><strong>Name category: </strong> {shop.category_supplier.name_category}</p>
              <p><strong>Level: </strong> {shop.category_supplier.level_category}</p>
            </div>
          )}
          <p>_________________</p>
          <p>Debt to supplier: {shop.debt_to_supplier} BYN</p>
          <p>Created at: {shop.created_at}</p>
          <button onClick={() => copyEmail(shop.email)}>Копировать email</button>
          <hr />
        </div>
      ))}
    </div>
  );
}

export default App;
