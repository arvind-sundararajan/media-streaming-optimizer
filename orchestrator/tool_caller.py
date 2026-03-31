```json
{
    "orchestrator/tool_caller.py": {
        "content": "
import logging
from typing import Dict, List
from allennlp.common.util import logger
from letta import LettaAgent, MemoryManagement
from stumpy import stochastic_regime_switch

class ToolCaller:
    def __init__(self, agent: LettaAgent, tools: List[str]):
        """
        Initialize the ToolCaller with a LettaAgent and a list of tools.

        Args:
        - agent (LettaAgent): The LettaAgent to use for tool calling.
        - tools (List[str]): A list of tools to use for the agent.
        """
        self.agent = agent
        self.tools = tools
        self.memory_management = MemoryManagement(self.agent)

    def call_tool(self, tool: str, params: Dict[str, str]) -> str:
        """
        Call a tool with the given parameters.

        Args:
        - tool (str): The tool to call.
        - params (Dict[str, str]): A dictionary of parameters to pass to the tool.

        Returns:
        - str: The result of the tool call.
        """
        try:
            logging.info(f'Calling tool {tool} with params {params}')
            result = self.agent.call_tool(tool, params)
            self.memory_management.update_memory(result)
            return result
        except Exception as e:
            logging.error(f'Error calling tool {tool}: {e}')
            raise

    def stochastic_regime_switch(self, data: List[float]) -> float:
        """
        Apply stochastic regime switch to the given data.

        Args:
        - data (List[float]): A list of data points.

        Returns:
        - float: The result of the stochastic regime switch.
        """
        try:
            logging.info(f'Applying stochastic regime switch to data {data}')
            result = stochastic_regime_switch(data)
            return result
        except Exception as e:
            logging.error(f'Error applying stochastic regime switch: {e}')
            raise

    def non_stationary_drift_index(self, data: List[float]) -> float:
        """
        Calculate the non-stationary drift index for the given data.

        Args:
        - data (List[float]): A list of data points.

        Returns:
        - float: The non-stationary drift index.
        """
        try:
            logging.info(f'Calculating non-stationary drift index for data {data}')
            result = self.agent.calculate_non_stationary_drift_index(data)
            return result
        except Exception as e:
            logging.error(f'Error calculating non-stationary drift index: {e}')
            raise

def main():
    # Create a LettaAgent
    agent = LettaAgent()

    # Create a ToolCaller with the agent and a list of tools
    tool_caller = ToolCaller(agent, ['tool1', 'tool2'])

    # Call a tool
    result = tool_caller.call_tool('tool1', {'param1': 'value1'})
    print(result)

    # Apply stochastic regime switch
    data = [1.0, 2.0, 3.0]
    result = tool_caller.stochastic_regime_switch(data)
    print(result)

    # Calculate non-stationary drift index
    result = tool_caller.non_stationary_drift_index(data)
    print(result)

if __name__ == '__main__':
    main()
",
        "commit_message": "feat: implement specialized tool_caller logic"
    }
}
```