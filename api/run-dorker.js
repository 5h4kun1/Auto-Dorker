const { execSync } = require('child_process');

module.exports = async (req, res) => {
  const { website, dorkSelection } = req.query;
  
  try {
    const command = `python3 dork.py ${website} ${dorkSelection}`;
    const result = execSync(command, { encoding: 'utf-8' });
    res.status(200).send(result);
  } catch (error) {
    res.status(500).send(`Error executing dork.py: ${error.message}`);
  }
};

