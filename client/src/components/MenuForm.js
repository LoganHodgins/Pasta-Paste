import TextBox from "./TextBox";
import Button from "./Button";
import UserSelect from "./UserSelect";

const MenuForm = () => {
  return (
    <form>
      <TextBox />
      <label>Paste Name</label>
      <input type="text"></input>
      <label>Tags</label>
      <UserSelect options={['Plain Text', 'Code', 'Machine Learning']}/>
      <label>Syntax Highlighting</label>
      <UserSelect options={['Plain Text', 'Python']}/>
      <Button type='submit'>Submit Paste</Button>
    </form>
  );
};

export default MenuForm;