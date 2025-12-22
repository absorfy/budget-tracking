import React from "react";

function UserProfile({ balance }) {
  return (
    <div className="user-profile">
      <h2>Баланс: {balance} грн</h2>
    </div>
  );
}

export default UserProfile;
