import React from "react";

function TransactionList({ transactions }) {
  return (
    <div className="transaction-list">
      <h2>Мої транзакції</h2>
      <ul>
        {transactions.map((t) => (
          <li key={t.id} className={t.type === "Доходи" ? "income" : "expense"}>
            <span>{t.description}</span>
            <span>{t.amount} грн</span>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default TransactionList;
