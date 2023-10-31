library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;


entity FreqDiv_16 is
    port(CLK_Input : in std_logic;
	      Freq2,Freq4,Freq8,Freq16 : out std_logic);
end FreqDiv_16;

architecture behave of FreqDiv_16 is
  signal count : std_logic_vector(3 downto 0); 
begin
  process(CLK_Input)
  begin
    if(CLK_Input'event and CLK_Input = '1') then
	   if(count = "1111") then
		  count <= (others => '0');
		else
		  count <= count + 1;
		end if;
	 end if;
  end process;
  Freq2 <= count(0);
  Freq4 <= count(1);
  Freq8 <= count(2);
  Freq16<= count(3);
end behave;
