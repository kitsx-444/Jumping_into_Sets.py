active = {'EURUSD', 'GBPUSD', 'USDJPY', 'AUDUSD', 'USDCAD'}
archive = {'EURUSD', 'USDCHF', 'NZDUSD', 'GBPUSD'}

in_both = active & archive
active_pairs = active - archive
universal_pairs = active_pairs | archive
user_input = input('Enter a currency pair: ').upper()

if user_input in active:
	print('This pair is currently active.')
else:
	print('This pair is not currently active.')

print(f'\nIn both watchlists: {in_both}')
print(f'Only in active: {active_pairs}')
print(f'Universal watchlist: {universal_pairs}')
