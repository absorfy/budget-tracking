<div className="dashboard">

  <h1>Особистий кабінет</h1>

  <div className="balance">
    Баланс: 900 грн
  </div>

  <div className="transaction-form">
    <select>
      <option>Доходи</option>
      <option>Витрати</option>
    </select>

    <input type="number" placeholder="Сума" />
    <input type="text" placeholder="Опис" />

    <button>Додати</button>
  </div>

  <h2>Мої транзакції</h2>

  <div className="transactions">
    <div className="transaction-item income">
      <div className="transaction-left">
        <span className="transaction-title">Зарплата</span>
        <span className="transaction-type">Доходи</span>
      </div>
      <strong>+1200 грн</strong>
    </div>

    <div className="transaction-item expense">
      <div className="transaction-left">
        <span className="transaction-title">Продукти</span>
        <span className="transaction-type">Витрати</span>
      </div>
      <strong>-300 грн</strong>
    </div>

    <div className="transaction-item expense">
      <div className="transaction-left">
        <span className="transaction-title">Рахунок</span>
        <span className="transaction-type">Витрати</span>
      </div>
      <strong>-77 грн</strong>
    </div>
  </div>

</div>