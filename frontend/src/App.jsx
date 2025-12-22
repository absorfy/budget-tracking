import { useEffect, useState } from "react";
import "./App.css";

export default function App() {
  const [transactions, setTransactions] = useState(() => {
    const saved = localStorage.getItem("transactions");
    return saved ? JSON.parse(saved) : [];
  });

  const [type, setType] = useState("income");
  const [amount, setAmount] = useState("");
  const [title, setTitle] = useState("");

  const balance = transactions.reduce((acc, t) => {
    return t.type === "income" ? acc + t.amount : acc - t.amount;
  }, 0);

  
  useEffect(() => {
    localStorage.setItem("transactions", JSON.stringify(transactions));
  }, [transactions]);


  const addTransaction = () => {
    if (!amount || !title) return;

    const newTransaction = {
      id: Date.now(),
      type,
      title,
      amount: Number(amount),
    };

    setTransactions([newTransaction, ...transactions]);
    setAmount("");
    setTitle("");
  };


  const deleteTransaction = (id) => {
    setTransactions(transactions.filter(t => t.id !== id));
  };

  return (
    <div className="dashboard">
      <h1>Особистий кабінет</h1>

      <div className="balance">
        Баланс: {balance} грн
      </div>

      {/* FORM */}
      <div className="transaction-form">
        <select value={type} onChange={e => setType(e.target.value)}>
          <option value="income">Доходи</option>
          <option value="expense">Витрати</option>
        </select>

        <input
          type="number"
          placeholder="Сума"
          value={amount}
          onChange={e => setAmount(e.target.value)}
        />

        <input
          type="text"
          placeholder="Опис"
          value={title}
          onChange={e => setTitle(e.target.value)}
        />

        <button onClick={addTransaction}>Додати</button>
      </div>

      {/* LIST */}
      <h2>Мої транзакції</h2>

      <div className="transactions">
        {transactions.map(t => (
          <div key={t.id} className={`transaction-item ${t.type}`}>
            <div className="icon">
              {t.type === "income" ? "💰" : "🛒"}
            </div>

            <div className="transaction-left">
              <span className="transaction-title">{t.title}</span>
              <span className="transaction-type">
                {t.type === "income" ? "Доходи" : "Витрати"}
              </span>
            </div>

            <strong>
              {t.type === "income" ? "+" : "-"}
              {t.amount} грн
            </strong>

            <button
              className="delete-btn"
              onClick={() => deleteTransaction(t.id)}
            >
              ✕
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}