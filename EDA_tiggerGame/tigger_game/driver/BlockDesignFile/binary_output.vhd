library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity binary_output is
  port (
    input : in std_logic; -- �����ź�
    output1 : out std_logic_vector(5 downto 0); -- ���1
    output2 : out std_logic_vector(5 downto 0); -- ���2
    output3 : out std_logic_vector(5 downto 0); -- ���3
    output4 : out std_logic_vector(5 downto 0) -- ���4
  );
end binary_output;

architecture behav of binary_output is
begin
  process (input)
  begin
    if input = '0' then -- �������Ϊ1
      output1 <= "010000"; -- ���1Ϊ16
      output2 <= "001010"; -- ���2Ϊ10
      output3 <= "010110"; -- ���3Ϊ22
      output4 <= "001110"; -- ���4Ϊ14
    else -- �������Ϊ0������ֵ
      output1 <= "011000"; -- ���1Ϊ24
      output2 <= "011111"; -- ���2Ϊ31
      output3 <= "001110"; -- ���3Ϊ14
      output4 <= "011011"; -- ���4Ϊ27
    end if;
  end process;
end behav;