library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity binary_output is
  port (
    input : in std_logic; -- 输入信号
    output1 : out std_logic_vector(5 downto 0); -- 输出1
    output2 : out std_logic_vector(5 downto 0); -- 输出2
    output3 : out std_logic_vector(5 downto 0); -- 输出3
    output4 : out std_logic_vector(5 downto 0) -- 输出4
  );
end binary_output;

architecture behav of binary_output is
begin
  process (input)
  begin
    if input = '0' then -- 如果输入为1
      output1 <= "010000"; -- 输出1为16
      output2 <= "001010"; -- 输出2为10
      output3 <= "010110"; -- 输出3为22
      output4 <= "001110"; -- 输出4为14
    else -- 如果输入为0或其他值
      output1 <= "011000"; -- 输出1为24
      output2 <= "011111"; -- 输出2为31
      output3 <= "001110"; -- 输出3为14
      output4 <= "011011"; -- 输出4为27
    end if;
  end process;
end behav;
