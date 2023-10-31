--Scan_Display2021.09.30
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity Scan_Disp is
	port
	(	ScanClk	  : in std_logic;
		Din0,Din1,Din2,Din3 : in integer range 0 to 9;
		Din4,Din5,Din6,Din7 : in integer range 0 to 9;
		DP		 : out std_logic;
		DigData  : out std_logic_vector (7 DOWNTO 0);
		SegData  : out std_logic_vector (6 DOWNTO 0));
end entity;

architecture rtl of Scan_Disp is
signal LedCode : integer range 0 to 15;
begin
	process (ScanClk)
	variable cnt : integer range 0 to 7;
	begin
		if (rising_edge(ScanClk)) then
				cnt := cnt + 1;
		end if;
		case cnt is  --selection of position,data and digital point
			when 0 =>DigData<="11111110"; LedCode<=Din0;DP<='1';  
			when 1 =>DigData<="11111101"; LedCode<=Din1;DP<='1';  
			when 2 =>DigData<="11111011"; LedCode<=Din2;DP<='1';  
			when 3 =>DigData<="11110111"; LedCode<=Din3;DP<='1';  
			when 4 =>DigData<="11101111"; LedCode<=Din4;DP<='1';  
			when 5 =>DigData<="11011111"; LedCode<=Din5;DP<='1';  
			when 6 =>DigData<="10111111"; LedCode<=Din6;DP<='1';  
			when 7 =>DigData<="01111111"; LedCode<=Din7;DP<='1';  
		end case;
	end process;
	process (LedCode) --display decoder for common-anode LED
	begin
		case LedCode is      --gfedcba  
			when 0 =>SegData<="1000000"; --display 0
			when 1 =>SegData<="1111001";
			when 2 =>SegData<="0100100";
			when 3 =>SegData<="0110000";
			when 4 =>SegData<="0011001";
			when 5 =>SegData<="0010010";
			when 6 =>SegData<="0000010";
			when 7 =>SegData<="1111000";
			when 8 =>SegData<="0000000";
			when 9 =>SegData<="0010000";
			when others =>SegData<="1111111"; --display nothing
		end case;
	end process;
end rtl;

