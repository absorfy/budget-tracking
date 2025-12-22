import React, { useState } from "react";

function AddTransactionForm({ onAdd }) {
  const [type, setType] = useState("Доходи");
  const [amount, setAmount] = useState("");
  const [description, setDescription] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!amount || !description) return;
    onAdd({ type, amount: parseFloat(amount), description });
    setAmount("");
    setDescription("");
  };

  return (
    <form className="add-transaction" onSubmit={handleSubmit}>
      <select value={type} onChange={(e) => setType(e.target.value)}>
        <option>Доходи</option>
        <option>Витрати</option>
      </select>
      <input
        type="number"
        placeholder="Сума"
        value={amount}
        onChange={(e) => setAmount(e.target.value)}
      />
      <input
        type="text"
        placeholder="Опис"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
      />
      <button type="submit">Додати</button>
    </form>
  );
}

export default AddTransactionForm;
