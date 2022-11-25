const UserSelect = (props) => {
  let options = props.options.map((option) => <option>{option}</option>);

  return (
    <select>
      {options}
    </select>
  );
};

export default UserSelect;