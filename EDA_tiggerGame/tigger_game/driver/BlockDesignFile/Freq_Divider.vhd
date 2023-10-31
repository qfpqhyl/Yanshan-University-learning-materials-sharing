-- Freqency Divider Designd by Huang 2021.09.29
-- Source clock 50MHz,divided frequencies of 1MHz,1kHz,100Hz,10Hz and 1Hz provided
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity Freq_Divider is
	port
	(	clkin	  : in std_logic;
		--q		  : out integer range 0 to 999;		--noly for test
		clkout1M,clkout1k,clkout100,clkout10,clkout1  : out std_logic);
end entity;

architecture rtl of Freq_Divider is
signal sclkout1M,sclkout1k,sclkout100,sclkout10,sclkout1  : std_logic;
begin
	process (clkin)--1MHz = 50MHz divied by 50
		variable   cnt		   : integer range 0 to 49;		
	begin
		if (rising_edge(clkin)) then
				if cnt <49 then cnt := cnt + 1; else cnt :=0; end if; 
				if cnt <25 then sclkout1M<='0'; else sclkout1M<='1';end if;
		end if;
	end process;
	process (sclkout1M)--1kHz = 1MHz divied by 1000
		variable   cnt		   : integer range 0 to 999;		
	begin
		if (rising_edge(sclkout1M)) then
				if cnt <999 then cnt := cnt + 1; else cnt :=0; end if; 
				if cnt <500 then sclkout1k<='0'; else sclkout1k<='1';end if;
		end if;
	end process;
	process (sclkout1k)--100Hz = 1kHz divied by 10
		variable   cnt		   : integer range 0 to 9;		
	begin
		if (rising_edge(sclkout1k)) then
				if cnt <9 then cnt := cnt + 1; else cnt :=0; end if; 
				if cnt <5 then sclkout100<='0'; else sclkout100<='1';end if;
		end if;
	end process;	
	process (sclkout100)--10Hz = 100Hz divied by 10
		variable   cnt		   : integer range 0 to 9;		
	begin
		if (rising_edge(sclkout100)) then
				if cnt <9 then cnt := cnt + 1; else cnt :=0; end if; 
				if cnt <5 then sclkout10<='0'; else sclkout10<='1';end if;
		end if;
	end process;		
	process (sclkout10)--1Hz = 10Hz divied by 10
		variable   cnt		   : integer range 0 to 9;		
	begin
		if (rising_edge(sclkout10)) then
				if cnt <9 then cnt := cnt + 1; else cnt :=0; end if; 
				if cnt <5 then sclkout1<='0'; else sclkout1<='1';end if;
		end if;
		--q <= cnt;	--only for test
	end process;
	clkout1M<=sclkout1M;	clkout1k<=sclkout1k;	clkout100<=sclkout100;
	clkout10<=sclkout10;	clkout1<=sclkout1;
end rtl;

