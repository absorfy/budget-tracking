import { useEffect, useState } from "react";
import "./App.css";
import { api } from "./api/api";

export default function App() {
    const [wallet, setWallet] = useState(null);
    const [transactions, setTransactions] = useState([]);
    const [type, setType] = useState("income");
    const [amount, setAmount] = useState("");
    const [title, setTitle] = useState("");
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const balance = wallet ? Number(wallet.balance) : 0;

    useEffect(() => {
        const init = async () => {
            setLoading(true);
            try {
                const wallets = await api.getWallets();
                let active = wallets[0];
                if (!active) {
                    active = await api.createWallet({ name: "Main Wallet" });
                }
                setWallet(active);
                await loadTransactions(active.id);
                setError(null);
            } catch (e) {
                setError(e.message);
            } finally {
                setLoading(false);
            }
        };
        init();
    }, []);

    const loadTransactions = async (walletId) => {
        if (!walletId) return;
        setLoading(true);
        try {
            const data = await api.getTransactions(walletId);

            setTransactions(data.map(t => ({ ...t, amount: Number(t.amount) })));
            setError(null);
        } catch (e) {
            setError(e.message);
        } finally {
            setLoading(false);
        }
    };


    const addTransaction = () => {
        if (!amount || !title || !wallet) return;
        const payload = {
            wallet: wallet.id,
            type,
            amount: Number(amount),
            description: title,
        };
        api.createTransaction(payload)
            .then(async () => {
                await loadTransactions(wallet.id);
                const freshWallet = await api.getWallet(wallet.id);
                setWallet(freshWallet);
                setAmount("");
                setTitle("");
            })
            .catch((e) => setError(e.message));
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

                <button onClick={addTransaction} disabled={loading || !wallet}>Додати</button>
            </div>

            {/* LIST */}
            <h2>Мої транзакції</h2>

            {error && <div className="error">{error}</div>}
            {loading && <div className="loading">Завантаження...</div>}

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