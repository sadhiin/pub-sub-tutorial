# Main entry point for the trading system.  Allows running producer, consumer, or both.
import argparse
import threading
from src.producers.market_data_producer import create_kafka_producer, publish_market_data
from src.consumers.trading_consumer import run_consumer
from src.config.settings import KAFKA_BROKERS
import sys

def main():
    """
    Main function to parse command-line arguments and run the producer and/or consumer.
    """
    parser = argparse.ArgumentParser(description="Run the market data producer and/or consumer.")
    parser.add_argument("--producer", action="store_true", help="Run the producer.")
    parser.add_argument("--consumer", action="store_true", help="Run the consumer.")
    parser.add_argument("--both", action="store_true", help="Run both producer and consumer.")
    parser.add_argument("--num_events", type=int, default=20, help="Number of events to produce (for producer).")
    parser.add_argument("--symbols", nargs='+', default=['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA'],
                        help="List of stock symbols for the producer.")

    args = parser.parse_args()

    if not any([args.producer, args.consumer, args.both]):
        print("Please specify --producer, --consumer, or --both.")
        sys.exit(1)

    threads = []

    if args.producer or args.both:
        producer = create_kafka_producer() # Create the producer here
        producer_thread = threading.Thread(target=publish_market_data, args=(producer, args.symbols, args.num_events))
        threads.append(producer_thread)
        producer_thread.start()

    if args.consumer or args.both:
        consumer_thread = threading.Thread(target=run_consumer)
        threads.append(consumer_thread)
        consumer_thread.start()

    try:
        for thread in threads:
            thread.join()
    except KeyboardInterrupt:
        print("Program interrupted by user.")
    finally:
        print("Exiting...") # Make sure this line is reached
        if 'producer' in locals():
            producer.close() # Close producer

if __name__ == "__main__":
    main()