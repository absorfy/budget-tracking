import React, { useState } from "react";
import TransactionList from "./TransactionList";
import AddTransactionForm from "./AddTransactionForm";
import UserProfile from "./UserProfile";

function Dashboard() {
  const [transactions, setTransactions] = useState([
    { id: 1, type: "Доходи", amount: 1200, description: "Зарплата" },
    { id: 2, type: "Витрати", amount: 300, description: "Продукти" },
  ]);

  const addTransaction = (transaction) => {
    setTransactions([...transactions, { id: Date.now(), ...transaction }]);
  };

  const balance = transactions.reduce(
    (acc, t) => acc + (t.type === "Доходи" ? t.amount : -t.amount),
    0
  );

  return (
    <div className="dashboard">
      <UserProfile balance={balance} />
      <AddTransactionForm onAdd={addTransaction} />
      <TransactionList transactions={transactions} />
    </div>
  );
}

export default Dashboard;
