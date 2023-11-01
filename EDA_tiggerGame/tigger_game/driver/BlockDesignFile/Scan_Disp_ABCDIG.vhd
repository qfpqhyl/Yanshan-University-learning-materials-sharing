library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity Scan_Disp_ABCDIG is
	port
	(	ScanClk	  : in std_logic;
		Din0,Din1,Din2,Din3 : in integer range 0 to 9;
		Din4,Din5,Din6,Din7 : in integer range 10 to 35;
		DP		 : out std_logic;
		DigData  : out std_logic_vector (7 DOWNTO 0);
		SegData   : out std_logic_vector (6 DOWNTO 0));
end entity;

architecture rtl of Scan_Disp_ABCDIG is
signal LedCode : integer range 0 to 35;
begin
	process (ScanClk)
	variable cnt : integer range 0 to 7;
	begin
		if (rising_edge(ScanClk)) then
				cnt := cnt + 1;
		end if;
		case cnt is  
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
	process (LedCode) 
	begin
		case LedCode is      
			when 0 => SegData <="1000000";
			when 1 => SegData <="1111001";
			when 2 => SegData <="0100100";
			when 3 => SegData <="0110000";
			when 4 => SegData <="0011001";
			when 5 => SegData <="0010010";
			when 6 => SegData <="0000010";
			when 7 => SegData <="1111000";
			when 8 => SegData <="0000000";
			when 9 => SegData <="0010000";
            when 10 => SegData <= "0001000"; --display A 
			when 11 => SegData <="0000011"; --display b 
			when 12 => SegData <="1000111"; --display C 
			when 13 => SegData <="0000110"; --display d 
			when 14 => SegData <="0000110"; --display E 
			when 15 => SegData <="1001111"; --display F 
			when 16 => SegData <="0000010"; --display g 
			when 17 => SegData <="0001010"; --display H 
			when 18 => SegData <="1111101"; --display I 
			when 19 => SegData <="0001110"; --display J 
			when 20=> SegData <="0011010"; --display K 
			when 21 => SegData <="1100011"; --display L 
			when 22 => SegData <="0101010"; --display M 
			when 23 => SegData <="0001010"; --display n 
			when 24 => SegData <="1000000"; --display o 
			when 25 => SegData <="0101000"; --display P 
			when 26 => SegData <="0110011"; --display q 
			when 27 => SegData <="0001000"; --display r 
			when 28 => SegData <="0010010"; --display S 
			when 29 => SegData <="1110001"; --display t 
			when 30 => SegData <="0001110"; --display U 
			when 31 => SegData <="1000001"; --display v 
			when 32 => SegData <="0001101"; --display W 
			when 33 => SegData <="0011110"; --display X 
			when 34 => SegData <="0110110"; --display y 
			when 35 => SegData <="0100100"; --display Z        
			when others => SegData <="1111111"; --display nothing
		end case;
	end process;
end rtl;
--if make GAME or OVER in 7-4,the point should input 16,10,22,14 or 24,31,14,27